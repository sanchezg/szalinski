def test_index_GET_wout_code_returns_main_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_index_POST_returns_index_rendered_with_url(client):
    TEST_URL = "https://some.long.url/"
    response = client.post("/", json={"url": TEST_URL})
    response_data = response.json()

    assert response.status_code == 200
    assert "url" in response_data
    assert "url_hash" in response_data
    assert response_data["url"] == TEST_URL


def test_index_GET_url_not_exists_returns_404(client):
    response = client.get("/some-missing-hash")
    response_data = response.json()

    assert response.status_code == 404
    assert response_data["detail"] == "URL hash not found"
