# SHA256-SERVICE

This service provides two endpoints:

- POST `/messages`: Generating SHA256 hashes from strings
- GET `/messages/{hash}`: Retrieving strings from hashes if available

## Create Hash

### Request [POST] /messages

```json
{
    "message" : "string"
}
```

### Response

```json
{
    "hash" : "string"
}
```

## Retrieve Message

### Request [GET] /messages/{hash}

### Response

```json
{
    "message" : "string"
}
```

If no message is retrieved given the hash `Error 404` is returned.

## Deployment

To run the app, You need to provide AWS credentials in a `.env` file

### `.env` file

```env
DB_REGION_NAME=<aws-region>
DB_ACCESS_KEY_ID=<aws-access-key-id>
DB_SECRET_ACCESS_KEY=<aws-secret-key-id>
```

After creating `.env` file, you can run the application using docker-compose:

```bash
$> docker-compose up -d
```

You can view API documentations after running the application at

- `<url>/docs`
- `<url>/redoc/`

if running locally, you can use `http://localhost` instead of `<url>`.
