import json


def read_json(file_name):

    with open(file_name) as f:
        data = json.load(f)

    return data


def check_amplify(genes):

    output_dict = {}
    for key, val in genes.items():
        if len(val) < 1:
            output_dict[key] = False
            continue
        else:
            amp_exons = []
            exons_num = -1
            for i in val:
                if len(i) > 0:
                    exons_num = int(i.split('/')[1])
                    exon_range = i.split('/')[0].split('-')
                    amp_exons.extend(range(int(exon_range[0]), int(exon_range[1])+1))

            if len(amp_exons) == exons_num:
                output_dict[key] = True
            else:
                output_dict[key] = False
    return output_dict


if __name__ == '__main__':

    file_name = 'test_data.json'

    output = check_amplify(read_json(file_name))
    print(output)