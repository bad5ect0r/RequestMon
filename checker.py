from selftest import SelfTest

import argparse
import os
import pushover


PYGMENTS_STYLES = ["vs", "xcode"] 
REQUEST_OBJECTS = [SelfTest]


if __name__ == '__main__':
    description = """Given two source files this application\
    creates an html page which highlights the differences between the two. """

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-s', '--show', action='store_true',
                        help='show html in a browser.')
    parser.add_argument('-p', '--print-width', action='store_true', 
        help='Restrict code to 80 columns wide. (printer friendly in landscape)')
    parser.add_argument('-c', '--syntax-css', action='store', default="vs",
        help='Pygments CSS for code syntax highlighting. Can be one of: %s' % str(PYGMENTS_STYLES))
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output.')

    args = parser.parse_args()

    if args.syntax_css not in PYGMENTS_STYLES:
        raise ValueError("Syntax CSS (-c) must be one of %r." % PYGMENTS_STYLES)

    for obj in REQUEST_OBJECTS:
        t = obj()
        if t.is_x_files_present(1):
            t.perform_request()

            files = os.listdir(t.save_path)
            files = list(map(int, files))
            files.sort()
            latest = files.pop()
            isdifferent = t.is_different_to_file(t.save_path + str(latest))

            if isdifferent:
                t.save()
                t.generate_diff(t.save_path + str(latest), args)
                pushover.send_message('Change Detected in {}'.format(t.url), 'Diff at {}'.format(t.diff_path))
        else:
            t.perform_request()
            t.save()

