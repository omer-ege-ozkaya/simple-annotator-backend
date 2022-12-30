import pymongo, json

mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
annotation_database = mongo_client["annotation_database"]
annotation_collection = annotation_database["annotations"]
annotation_collection.drop()


def get_list_of_annotations():
    list_of_annotations = [annotation for annotation in annotation_collection.find()]
    print("Listing", list_of_annotations)
    return list_of_annotations


def get_annotation(_id: str):
    print("Getting", _id)
    annotation_mapping = annotation_collection.find_one({"_id": _id})
    if annotation_mapping is None:
        return None
    annotation_dict = dict(annotation_mapping)
    annotation_dict["id"] = annotation_dict.pop("_id")
    print("Got", annotation_dict)
    return annotation_dict


def insert_annotation(annotation_dict: dict):
    print("Inserting", annotation_dict)
    annotation_collection.insert_one(annotation_dict)


def update_annotation(annotation_dict: dict):
    print("Updating", annotation_dict)
    annotation_collection.insert_one(annotation_dict)


def upsert_annotation(_id: str, annotation_dict: dict):
    print("Upserting", annotation_dict)
    annotation_dict["_id"] = annotation_dict.pop("id")
    if get_annotation(_id) is None:
        insert_annotation(annotation_dict)
    else:
        update_annotation(annotation_dict)


def delete_annotation(_id: str):
    print("Deleting", _id)
    if get_annotation(_id) is not None:
        pass


# print(get_list_of_annotations())
# print(get_annotation("12318"))
#
# annotation = {"_id": "12318", "annotation": "AnnotationJson", "whatever": {"asdf": "asdf"}}
#
# print("ege", json.dumps(get_list_of_annotations()))
#
# x = annotation_collection.insert_one(annotation)
# print(x)
# print(x.inserted_id)
# print(get_annotation("12318"))
# y = annotation_collection.find()
# for x in annotation_collection.find():
#     print(x)
