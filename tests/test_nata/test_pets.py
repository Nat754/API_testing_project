import requests
import pytest
import allure
from tests.test_nata.constant_nata import PET_URL, FIND_BY_STATUS, UPDATE_PET
from data.status_code import StatusCode


@allure.epic("Test for pet")
class TestPet:
    status_code = StatusCode()

    @allure.title("get_finds_pets_by_status")
    @pytest.mark.parametrize('status', ['pending', 'available', 'sold'])
    def test_get_finds_pets_by_status(self, status):
        url = f'{PET_URL}{FIND_BY_STATUS}{status}'
        response = requests.get(url=url)
        assert response.status_code == self.status_code.STATUS_OK, \
            f"Expected status {self.status_code.STATUS_OK}, actual status {response.status_code}"

    @allure.title("post_add_a_new_pet_to_the_store")
    def test_post_add_a_new_pet_to_the_store(self, add_new_pet):
        assert add_new_pet.status_code == self.status_code.STATUS_OK, "Wrong status code"

    @allure.title("get_pet_by_id")
    def test_get_pet_by_id(self, add_new_pet):
        url = f'{PET_URL}777'
        response = requests.get(url)
        assert response.status_code == self.status_code.STATUS_OK, \
            f"Expected status {self.status_code.STATUS_OK}, actual status {response.status_code}"

    @pytest.mark.xfail(reason="Undocumented status code")
    @allure.title("post_uploads_an_image_pet")
    def test_post_uploads_an_image_pet(self, add_new_pet):
        url = f'{PET_URL}777/uploadImage'
        response = requests.post(url)
        print(response.text)
        assert response.status_code == self.status_code.STATUS_OK, \
            f"Expected status {self.status_code.STATUS_OK}, actual status {response.status_code}"

    @allure.title('put_update_an_existing_pet')
    def test_put_update_an_existing_pet(self, add_new_pet):
        url = PET_URL
        response = requests.put(url, json=UPDATE_PET)
        assert response.status_code == self.status_code.STATUS_OK, \
            f"Expected status {self.status_code.STATUS_OK}, actual status {response.status_code}"
