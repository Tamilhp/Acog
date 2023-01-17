

class PreProcessor:
    @staticmethod
    def process(input_file: str) -> str:
        """This function takes a file as input and converts it into a generator object(an iterator)"""
        with open(input_file, 'r+') as fp:
            while True:
                line: str = fp.readline()
                yield line
                if line == '':
                    return



