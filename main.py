import csv

def tuple_list_generator(old_list):
    new_list = []
    for value in set(old_list):
        key = 1 if len(new_list) == 0 else len(new_list) + 1
        new_list.append((key, value))

    return new_list

def create_csv(file_name, data):
    with open(f"{file_name}.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(["id", "name"])

        for item in data:
            csv_writer.writerow([item[0], item[1]])


def main():
    with open("address_list.csv", "r") as address_list_csv:
        address_list = csv.DictReader(address_list_csv)

        __regions = []
        __provinces = []
        __cities = []
        __barangays = []

        for address in address_list:
            __region = address["region"]
            __province = address["province"]
            __city = address["city"]
            __barangay = address["name"]

            __regions.append(__region)
            __provinces.append(__province)
            __cities.append(__city)
            __barangays.append(__barangay)

        regions = tuple_list_generator(__regions)
        provinces = tuple_list_generator(__provinces)
        cities = tuple_list_generator(__cities)
        barangays = tuple_list_generator(__barangays)

        create_csv("regions", regions)
        create_csv("provinces", provinces)
        create_csv("cities", cities)
        create_csv("barangays", barangays)

        # with open("barangays.csv", "r") as address_list_csv:
        #     address_list = csv.DictReader(address_list_csv)

        #     for address in address_list:
        #         for region in regions:
        #             if address['region'] == region[1]:
        #                 print(f"INSERT INTO province (name, region_id) VALUES ({address['province']}, {region[0]});")

        #         for province in provinces:
        #             if address['province'] == province[1]:
        #                 print(f"INSERT INTO city (name, region_id) VALUES ({address['city']}, {province[0]});")
                
        #         for city in cities:
        #             if address['city'] == city[1]:
        #                 print(f"INSERT INTO city (name, region_id) VALUES ({address['name']}, {city[0]});")



if __name__ == "__main__":
    main()