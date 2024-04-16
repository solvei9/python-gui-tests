from random import randrange


def test_del_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) == 1:
        app.groups.add_new_group("my group " + str(randrange(0, 99)))
        old_list = app.groups.get_group_list()
    index = randrange(len(old_list))
    app.groups.delete_group(index)
    new_list = app.groups.get_group_list()
    del old_list[index]
    assert sorted(old_list) == sorted(new_list)
