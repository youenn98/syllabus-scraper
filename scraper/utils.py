import re
import datetime
import unicodedata
import timeit

from scraper.const import location_name_map, dept_name_map


def rename_location(loc):
    """
    Renames the location of classrooms
    :param loc: location
    :return: location after renaming
    """
    if re.fullmatch(r"^[\d]+-[\d]+$", loc) is not None:
        return loc
    elif loc in location_name_map.keys():
        return location_name_map["loc"]
    else:
        return loc


def build_url(dept, page, lang):
    """
    Constructs the url of syllabus catalog page
    :param dept: department code
    :param page: page number
    :param lang: language ('en', 'jp')
    :return: str
    """
    param = dept_name_map[dept]["param"]
    year = datetime.datetime.now().year
    return f"https://www.wsl.waseda.jp/syllabus/JAA103.php?pYear={year}&p_gakubu={param}&p_page={page}&p_number=100&pLng={lang}"


def to_half_width(s):
    """
    Converts zenkaku to hankaku
    :param s:
    :return:
    """
    return unicodedata.normalize('NFKC', s)


def timer(func):
    def measure(*args, **kwargs):
        start_time = timeit.default_timer()
        func(*args, **kwargs)
        elapsed = timeit.default_timer() - start_time
        print(f"{func.__name__} took {elapsed} seconds to complete.")
    return measure