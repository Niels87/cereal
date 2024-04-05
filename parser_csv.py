import csv

class ParserCSV():

    def __init__(self) -> None:
        pass
    
    
    def parse_csv(self, file_path: str) -> list[dict]:
        
        with open(file_path, 'r') as csvfile:
            list_reader = csv.reader(csvfile, delimiter=';')
            self._fieldnames = next(list_reader)
            #print(self._fieldnames)
            self._fieldtypes = next(list_reader)
            #print(self._fieldtypes)
            self._fieldnames_with_types = dict(zip(self._fieldnames, self._fieldtypes))
            
            
            dict_reader = csv.DictReader(
                csvfile, delimiter=';', 
                fieldnames=self._fieldnames,
            )
            self.csvdata: list[dict] = []
            for row in dict_reader:
                self.csvdata.append(row)
            
            return self.csvdata
    
    # def cast_string_to_float(self, string: str) -> float:
    #     return float(string)
        

def main():
    
    csv_parser = ParserCSV()
    csv_parser.parse_csv("Cereal.csv")
    row = csv_parser.csvdata[0]
    for kv in row:
        print(f"{kv} ({csv_parser._fieldnames_with_types[kv]}): {row[kv]}")

if __name__=="__main__":
    main()