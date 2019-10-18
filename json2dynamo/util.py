import os
from dynamodb_json import json_util as json


class JsonTransfromer:
    def transform_json_files(self, input_path: str, output_path: str):
        for json_file in self.get_json_files(input_path):
            with open(f"{input_path}/{json_file}", "r") as file:
                template_json = json.loads(file.read())
                self.write_file_to_folder(
                    json.dumps(template_json), output_path, json_file
                )

    @staticmethod
    def write_file_to_folder(data: dict, outpath: str, filename: str) -> list:
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        with open(f"{outpath}/{filename}", "w+") as file:
            file.write(data)
            file.close()

    @staticmethod
    def get_json_files(input_path: str):
        return [
            pos_json
            for pos_json in os.listdir(input_path)
            if pos_json.endswith(".json")
        ]
