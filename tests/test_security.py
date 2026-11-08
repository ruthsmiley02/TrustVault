import app as trustvault


def test_application_imports():
    assert trustvault.app is not None


def test_dashboard_requires_login():
    client = trustvault.app.test_client()

    response = client.get("/dashboard")

    assert response.status_code == 302
    assert "/login" in response.location
def test_user_cannot_download_another_users_document(
    tmp_path, monkeypatch
):
    import json

    documents_file = tmp_path / "documents.json"
    audit_file = tmp_path / "audit_logs.json"
    upload_folder = tmp_path / "uploads"
    upload_folder.mkdir()

    document = {
        "id": "test-document-123",
        "filename": "private.pdf",
        "stored_name": "private.pdf",
        "owner": "admin123",
        "shared_with": {}
    }

    documents_file.write_text(json.dumps([document]))
    audit_file.write_text("[]")

    monkeypatch.setattr(
        trustvault, "DOCUMENTS_FILE", documents_file
    )
    monkeypatch.setattr(
        trustvault, "AUDIT_LOGS_FILE", audit_file
    )
    monkeypatch.setattr(
        trustvault, "UPLOAD_FOLDER", upload_folder
    )

    client = trustvault.app.test_client()

    with client.session_transaction() as session:
        session["username"] = "user123"
        session["role"] = "user"

    response = client.get("/download/test-document-123")

    assert response.status_code == 302

    logs = json.loads(audit_file.read_text())

    assert any(
        log.get("action") == "UNAUTHORIZED_DOWNLOAD"
        for log in logs
    )
def test_user_cannot_delete_another_users_document(
    tmp_path, monkeypatch
):
    import json

    documents_file = tmp_path / "documents.json"
    audit_file = tmp_path / "audit_logs.json"
    upload_folder = tmp_path / "uploads"
    upload_folder.mkdir()

    document = {
        "id": "delete-test-123",
        "filename": "private.pdf",
        "stored_name": "private.pdf",
        "owner": "admin123",
        "shared_with": {}
    }

    documents_file.write_text(json.dumps([document]))
    audit_file.write_text("[]")

    (upload_folder / "private.pdf").write_text("Test document")

    monkeypatch.setattr(
        trustvault, "DOCUMENTS_FILE", documents_file
    )
    monkeypatch.setattr(
        trustvault, "AUDIT_LOGS_FILE", audit_file
    )
    monkeypatch.setattr(
        trustvault, "UPLOAD_FOLDER", upload_folder
    )

    client = trustvault.app.test_client()

    with client.session_transaction() as session:
        session["username"] = "user123"
        session["role"] = "user"

    response = client.post("/delete/delete-test-123")

    assert response.status_code == 302

    saved_documents = json.loads(documents_file.read_text())

    assert len(saved_documents) == 1
    assert saved_documents[0]["id"] == "delete-test-123"

    assert (upload_folder / "private.pdf").is_file()

    logs = json.loads(audit_file.read_text())

    assert any(
        log.get("action") == "UNAUTHORIZED_DELETE"
        for log in logs
    )
def test_user_cannot_share_another_users_document(
    tmp_path, monkeypatch
):
    import json

    documents_file = tmp_path / "documents.json"
    audit_file = tmp_path / "audit_logs.json"
    users_file = tmp_path / "users.json"
    upload_folder = tmp_path / "uploads"
    upload_folder.mkdir()

    document = {
        "id": "share-test-123",
        "filename": "private.pdf",
        "stored_name": "private.pdf",
        "owner": "admin123",
        "shared_with": {}
    }

    users = [
        {"username": "admin123"},
        {"username": "user123"}
    ]

    documents_file.write_text(json.dumps([document]))
    audit_file.write_text("[]")
    users_file.write_text(json.dumps(users))

    monkeypatch.setattr(
        trustvault, "DOCUMENTS_FILE", documents_file
    )
    monkeypatch.setattr(
        trustvault, "AUDIT_LOGS_FILE", audit_file
    )
    monkeypatch.setattr(
        trustvault, "USERS_FILE", users_file
    )
    monkeypatch.setattr(
        trustvault, "UPLOAD_FOLDER", upload_folder
    )

    client = trustvault.app.test_client()

    with client.session_transaction() as session:
        session["username"] = "user123"
        session["role"] = "user"

    response = client.post(
        "/share/share-test-123",
        data={
            "username": "admin123",
            "permission": "read"
        }
    )

    assert response.status_code == 302

    saved_documents = json.loads(documents_file.read_text())

    assert saved_documents[0]["shared_with"] == {}

    logs = json.loads(audit_file.read_text())

    assert any(
        log.get("action") == "UNAUTHORIZED_SHARE"
        for log in logs
    )
def test_normal_user_cannot_access_audit_logs():
    client = trustvault.app.test_client()

    with client.session_transaction() as session:
        session["username"] = "user123"
        session["role"] = "user"

    response = client.get("/audit-logs")

    assert response.status_code == 302
def test_viewer_cannot_access_upload():

    client = trustvault.app.test_client()

    with client.session_transaction() as session:
        session["username"] = "viewer123"
        session["role"] = "viewer"

    response = client.get("/upload")

    assert response.status_code == 302
    assert "/dashboard" in response.location

def test_viewer_cannot_download_unshared_document(
    tmp_path, monkeypatch
):
    import json

    documents_file = tmp_path / "documents.json"
    audit_file = tmp_path / "audit_logs.json"
    upload_folder = tmp_path / "uploads"
    upload_folder.mkdir()

    document = {
        "id": "viewer-test-123",
        "filename": "private.pdf",
        "stored_name": "private.pdf",
        "owner": "admin123",
        "shared_with": {}
    }

    documents_file.write_text(json.dumps([document]))
    audit_file.write_text("[]")

    monkeypatch.setattr(
        trustvault, "DOCUMENTS_FILE", documents_file
    )
    monkeypatch.setattr(
        trustvault, "AUDIT_LOGS_FILE", audit_file
    )
    monkeypatch.setattr(
        trustvault, "UPLOAD_FOLDER", upload_folder
    )

    client = trustvault.app.test_client()

    with client.session_transaction() as session:
        session["username"] = "viewer123"
        session["role"] = "viewer"

    response = client.get("/download/viewer-test-123")

    assert response.status_code == 302

    logs = json.loads(audit_file.read_text())

    assert any(
        log.get("action") == "UNAUTHORIZED_DOWNLOAD"
        for log in logs
    )

def test_viewer_cannot_delete_document(
    tmp_path, monkeypatch
):
    import json

    documents_file = tmp_path / "documents.json"
    audit_file = tmp_path / "audit_logs.json"
    upload_folder = tmp_path / "uploads"
    upload_folder.mkdir()

    document = {
        "id": "viewer-delete-123",
        "filename": "private.pdf",
        "stored_name": "private.pdf",
        "owner": "admin123",
        "shared_with": {}
    }

    documents_file.write_text(json.dumps([document]))
    audit_file.write_text("[]")

    (upload_folder / "private.pdf").write_text("Test document")

    monkeypatch.setattr(
        trustvault, "DOCUMENTS_FILE", documents_file
    )
    monkeypatch.setattr(
        trustvault, "AUDIT_LOGS_FILE", audit_file
    )
    monkeypatch.setattr(
        trustvault, "UPLOAD_FOLDER", upload_folder
    )

    client = trustvault.app.test_client()

    with client.session_transaction() as session:
        session["username"] = "viewer123"
        session["role"] = "viewer"

    response = client.post("/delete/viewer-delete-123")

    assert response.status_code == 302

    saved_documents = json.loads(documents_file.read_text())

    assert len(saved_documents) == 1
    assert (upload_folder / "private.pdf").is_file()

def test_viewer_cannot_share_document():
    client = trustvault.app.test_client()

    with client.session_transaction() as session:
        session["username"] = "viewer123"
        session["role"] = "viewer"

    response = client.post(
        "/share/test-document-123",
        data={
            "username": "user123",
            "permission": "read"
        }
    )

    assert response.status_code == 302
    assert "/dashboard" in response.location

def test_viewer_cannot_download_after_access_revoked(
    tmp_path, monkeypatch
):
    import json

    documents_file = tmp_path / "documents.json"
    audit_file = tmp_path / "audit_logs.json"
    upload_folder = tmp_path / "uploads"
    upload_folder.mkdir()

    document = {
        "id": "revoked-test-123",
        "filename": "private.pdf",
        "stored_name": "private.pdf",
        "owner": "user123",
        "shared_with": {}
    }

    documents_file.write_text(json.dumps([document]))
    audit_file.write_text("[]")

    client = trustvault.app.test_client()

    monkeypatch.setattr(
        trustvault, "DOCUMENTS_FILE", documents_file
    )
    monkeypatch.setattr(
        trustvault, "AUDIT_LOGS_FILE", audit_file
    )
    monkeypatch.setattr(
        trustvault, "UPLOAD_FOLDER", upload_folder
    )

    with client.session_transaction() as session:
        session["username"] = "viewer123"
        session["role"] = "viewer"

    response = client.get("/download/revoked-test-123")

    assert response.status_code == 302

    logs = json.loads(audit_file.read_text())

    assert any(
        log.get("action") == "UNAUTHORIZED_DOWNLOAD"
        for log in logs
    )
