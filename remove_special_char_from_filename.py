import os, string, re, sys

def list_all_files_path(folder_path):
    tmp_list = []
    if os.path.isdir(folder_path):
        for path, __, files in os.walk(folder_path):
            for filename in files:
                tmp_list.append(path + '/' + filename)
    return tmp_list

def remove_special_char_in_basename(list_path):
    del_chars = ['`', '#', '$', '%', '&', '\'', ':', ';', '<', '>', '~', 'é', 'è', 'ê', 'à', 'â', 'ù', 'Å', '’', 'à', 'é']

    del_chars_regex = re.compile(r'|'.join(del_chars))

    for path in list_path:
        tmp_res = del_chars_regex.findall(os.path.basename(path).lower())
        if len(tmp_res) > 1:
            print(os.path.basename(path))
            new_name = re.sub(del_chars_regex, '', os.path.basename(path).lower())
            act_path = os.path.dirname(path)
            new_path = os.path.join(act_path, new_name)
            os.rename(path, new_path)
            
if __name__ == "__main__":
    if len(sys.argv) == 2:
        list_path = list_all_files_path(sys.argv[1])
        remove_special_char_in_basename(list_path)