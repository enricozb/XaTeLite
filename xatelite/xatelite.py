import argparse
import os
import sys

from flask import Flask, send_from_directory
from os.path import basename, dirname, join, splitext
from subprocess import call


def pdflatex(path):
    out_dir = dirname(path)
    base_name = splitext(basename(path))[0]
    log_file = join(out_dir, '{}.xatelog'.format(base_name))

    ret = call("pdflatex -interaction=nonstopmode -shell-escape "
               "-output-directory={} {} > {}".format(out_dir, path, log_file),
               shell=True)
    if ret:
        return {'directory': out_dir,
                'filename': '{}.xatelog'.format(base_name),
                'mimetype': 'text/plain'}

    return {'directory': out_dir,
            'filename': '{}.pdf'.format(base_name),
            'mimetype': 'application/pdf'}


def latex_server(args):
    def serve():
        return send_from_directory(**pdflatex(tex_file))

    tex_file = get_root_dir(args.latex_file)

    app = Flask(__name__)
    app.route('/')(serve)
    return app


def get_root_dir(tex_file):
    if not os.path.isabs(tex_file):
        tex_file = os.path.join(os.getcwd(), tex_file)
    return tex_file


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("latex_file",
                        help="the latex file to be compiled and served")
    parser.add_argument("-p", "--port",
                        default=5000,
                        help="specify which port the webserver will run on")
    parser.add_argument("-q", "--quiet",
                        action="store_true",
                        help="suppress any Flask output")
    parser.add_argument("-qq", "--qquiet",
                        action="store_true",
                        help="suppress all output including running message")
    return parser.parse_args()


def main():
    args = parse_args()

    if args.qquiet:
        args.quiet = True
    else:
        print('Running on port {}, with pid {}'.format(args.port,
                                                       os.getpid()))

    if args.quiet:
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    latex_server(args).run(host='0.0.0.0', port=args.port)


if __name__ == '__main__':
    main()

