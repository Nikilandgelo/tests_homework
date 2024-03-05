import pytest
from dotenv import dotenv_values
from yandex_disk import create_folder_yandex_disk, check_exist_folder

env_values = dotenv_values('api_key.env')
@pytest.mark.parametrize(
    "folder_name, api_key, expected",
    [
        ["Test_Folder", None, 401],
        ["Test_Folder^&%#@!*()-~qqeerfggrrryyereuruehhhhhhhghfghrereureueuree7548ikkipo[o537737yhyd]fhfrrrueeufjj5448899hihi333yjhjnnnvrreree4584858iiku5433&&%$##%&****&F%???))%_;%):*(:gkkeIKGKI555858338878ITITTI4*F&*%(LKHKHTYJTJTTJ###*#^(^#(^(^#(**(%*##HG:::$:^&&::", env_values.get("YANDEX_TOKEN"), 400],
        ["Test_Folder", env_values.get("YANDEX_TOKEN"), 201],
        ["Test_Folder", env_values.get("YANDEX_TOKEN"), 409],
        ["Another_Folder", env_values.get("YANDEX_TOKEN"), 201],
    ]
)
def test_create(folder_name, api_key, expected):
    result = create_folder_yandex_disk(folder_name, api_key)
    assert result == expected


@pytest.mark.parametrize(
    "folder_name, api_key, expected",
    [
        ["Test_Folder", None, 401],
        ["Test_Folder", env_values.get("YANDEX_TOKEN"), 200],
        ["NotExistingFolder", env_values.get("YANDEX_TOKEN"), 404],
        ["Another_Folder", env_values.get("YANDEX_TOKEN"), 200],
    ]
)
def test_exists(folder_name, api_key, expected):
    result = check_exist_folder(folder_name, api_key)
    assert result == expected