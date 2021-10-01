from distutils.core import setup
import py2exe


def main():
      setup(zipfile=None, options={'py2exe': {'bundle_files': 1}}, windows=["sihs.py"])


if __name__ == "__main__":
      main()
