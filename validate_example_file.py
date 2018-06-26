import sys
import tixiwrapper


def main(example_path, schema_path):
    tixi_h = tixiwrapper.Tixi()
    tixi_h.openDocument(example_path)
    error_code = tixi_h.schemaValidateFromFile(schema_path)
    exit(error_code)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])