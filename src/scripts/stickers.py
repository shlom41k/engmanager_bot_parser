# -*- coding: utf-8 -*-


STIC_PRESS_F = [
    'CAACAgIAAxkBAAIDm150ULHsbMkbpW8oVU0facSdq_TOAALZAANOm2QCv_uFcUNz2a8YBA',
    'CAACAgIAAxkBAAIDs150U0lfS3PU3BD9ow--cUoTYqfgAAK5AANOm2QCfc73g--nd2YYBA',
    'CAACAgIAAxkBAAIDtF50U1FioGbqx9v7E8jgEnA5ZUOOAALcAANOm2QCAAFd_RuxHdcsGAQ',
    'CAACAgIAAxkBAAIDtV50U1N1sf5XiXp-UUZLAAGG7lOO3gAC2wADTptkAje9NtoyOUz5GAQ',
    'CAACAgIAAxkBAAIDtl50U1cek56weawwXaSJ2v31i5-5AAIkAQACTptkAgr1ryvCrHtNGAQ',
    'CAACAgIAAxkBAAIDt150U1uLmUY0pk67Kv_KNscqr4OwAAIgAQACTptkAgYUB2j3jKYpGAQ',
    'CAACAgIAAxkBAAIDuF50U16hscuGWeoW7FTZ4gRFu_ARAAInAQACTptkAiWwP_XD4584GAQ',
    'CAACAgIAAxkBAAIDuV50U18HzYpBsUxyx1F245b1Xks6AAIoAQACTptkApn0n5J6_DdlGAQ',
    'CAACAgIAAxkBAAIDul50U2IY2ESLgF3lfl9E1BFQiKtzAAItAQACTptkAu2jz7PlHgs_GAQ',
    'CAACAgIAAxkBAAIDvF50U2g-N4BZbR1yRNVtVu9Ds3f8AAJZAQACTptkAgw6elKqS8COGAQ',
]

FLAGS = {
    "Англия": ("England", b"\xF0\x9F\x87\xAC\xF0\x9F\x87\xA7"),
    "Германия": ("Germany", b"\xF0\x9F\x87\xA9\xF0\x9F\x87\xAA"),
    "Испания": ("Spain", b"\xF0\x9F\x87\xAA\xF0\x9F\x87\xB8"),
    "Россия": ("Russia", b"\xF0\x9F\x87\xB7\xF0\x9F\x87\xBA"),
    "Италия": ("Italy", b"\xF0\x9F\x87\xAE\xF0\x9F\x87\xB9"),
    "Франция": ("France", b"\xF0\x9F\x87\xAB\xF0\x9F\x87\xB7"),
    "Лига Чемпионов": ("Champions_League", b"\xE2\x9A\xBD"),
    "Лига Европы": ("Europa_League", b"\xF0\x9F\x8F\x86"),
    "ed": ("ED", b"\xF0\x9F\x9A\xA9"),
    "default": ("Default", b"\xE2\x9D\x94"),
}

COMMANDS = [country for country, _ in FLAGS.values()]

ADMIN_COMMANDS = {
    "'/admins'": "show administrators list and control commands",
    "'/blacklist'": "show unauthorized users",
    "'/whitelist'": "show authorized users",
    "'/adduser id'": "add user to whitelist",
    "'/deluser id'": "detele user from whitelist",
    "'/clear blacklist'": "delete all users from blacklist",
}


if __name__ == "__main__":
    pass
