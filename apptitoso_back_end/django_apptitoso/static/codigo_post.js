$.ajax({
    url: 'http://127.0.0.1:8000/upload_files',
    type: 'POST',
    data: {""},
    cache: false,
    dataType: 'json',
    processData: false, // Don't process the files
    contentType: false, // Set content type to false as jQuery will tell the server its a query string request
    success: onSuccess,
    error: onError
});
