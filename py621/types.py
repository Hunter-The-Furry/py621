from datetime import datetime, timezone

e621 = "https://e621.net/"
e926 = "https://e926.net/"

class File:
    pass

class Preview:
    pass

class Sample:
    pass

class Score:
    pass

class Tags:
    pass

class Flags:
    pass

class Relationships:
    pass

class Post:
    def __init__(self, api):
        self.api = api

class Pool:
    def __init__(self, api):
        self.api = api

    def getPosts(self):
        return self.api.getPoolPosts(self.id)

def ListToPost(List, api):
    ThisPost = Post(api)

    # Commence the manual hell of a list to object
    ThisPost.id = List["id"]
    ThisPost.created_at = datetime.strptime(List["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
    ThisPost.updated_at = datetime.strptime(List["updated_at"], "%Y-%m-%dT%H:%M:%S.%f%z")

    ThisPost.file = File()
    ThisPost.file.width = List["file"]["width"]
    ThisPost.file.height = List["file"]["height"]
    ThisPost.file.ext = List["file"]["ext"]
    ThisPost.file.size = List["file"]["size"]
    ThisPost.file.md5 = List["file"]["md5"]
    ThisPost.file.url = List["file"]["url"]

    ThisPost.preview = Preview()
    ThisPost.preview.width = List["preview"]["width"]
    ThisPost.preview.height = List["preview"]["height"]
    ThisPost.preview.url = List["preview"]["url"]

    ThisPost.sample = Sample()
    ThisPost.sample.has = List["sample"]["has"]
    ThisPost.sample.width = List["sample"]["width"]
    ThisPost.sample.height = List["sample"]["height"]
    ThisPost.sample.url = List["sample"]["url"]

    ThisPost.score = Score()
    ThisPost.score.up = List["score"]["up"]
    ThisPost.score.down = List["score"]["down"]
    ThisPost.score.total = List["score"]["total"]

    ThisPost.tags = Tags()
    ThisPost.tags.general = List["tags"]["general"]
    ThisPost.tags.species = List["tags"]["species"]
    ThisPost.tags.character = List["tags"]["character"]
    ThisPost.tags.artist = List["tags"]["artist"]
    ThisPost.tags.invalid = List["tags"]["invalid"]
    ThisPost.tags.lore = List["tags"]["lore"]
    ThisPost.tags.meta = List["tags"]["meta"]

    ThisPost.locked_tags = List["locked_tags"]
    ThisPost.change_seq = List["change_seq"]

    ThisPost.flags = Flags()
    ThisPost.flags.pending = List["flags"]["pending"]
    ThisPost.flags.flagged = List["flags"]["flagged"]
    ThisPost.flags.note_locked = List["flags"]["note_locked"]
    ThisPost.flags.status_locked = List["flags"]["status_locked"]
    ThisPost.flags.rating_locked = List["flags"]["rating_locked"]
    ThisPost.flags.deleted = List["flags"]["deleted"]

    ThisPost.rating = List["rating"]
    ThisPost.fav_count = List["fav_count"]
    ThisPost.sources = List["sources"]
    ThisPost.pools = List["pools"]

    ThisPost.relationships = Relationships()
    ThisPost.relationships.parent_id = List["relationships"]["parent_id"]
    ThisPost.relationships.has_children = List["relationships"]["has_children"]
    ThisPost.relationships.has_active_children = List["relationships"]["has_active_children"]
    ThisPost.relationships.children = List["relationships"]["children"]

    ThisPost.approver_id = List["approver_id"]
    ThisPost.uploader_id = List["uploader_id"]
    ThisPost.description = List["description"]
    ThisPost.comment_count = List["comment_count"]

    return ThisPost

def ListToPool(List, api):
    ThisPool = Pool(api)

    ThisPool.id = List["id"]
    ThisPool.name = List["name"]
    ThisPool.created_at = datetime.strptime(List["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
    ThisPool.updated_at = datetime.strptime(List["updated_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
    ThisPool.creator_id = List["creator_id"]
    ThisPool.description = List["description"]
    ThisPool.is_active = List["is_active"]
    ThisPool.category = List["category"]
    ThisPool.is_deleted = List["is_deleted"]
    ThisPool.post_ids = List["post_ids"]
    ThisPool.creator_name = List["creator_name"]
    ThisPool.post_count = List["post_count"]

    return ThisPool