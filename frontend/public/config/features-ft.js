// defaults

window.tfrs_config = {
  'keycloak.authority': 'http://keycloak:8080/auth/realms/tfrs',
  'keycloak.client_id': 'tfrs-app',
  'keycloak.callback_url': 'http://nginx:10920/authCallback',
  'keycloak.post_logout_url': 'http://nginx:5001/',
  'debug.enabled': true,
  'secure_document_upload.enabled': true,
  'secure_document_upload.max_file_size': 50000000
};
