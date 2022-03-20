# shipwreck
An experiment with azure-storage-blob and using blob storage as an asset repository.

## Usage

`pip install shipwreck`

Two commands.

`ship pull`

Updates your local directory with the files from the recording.json.

`ship push`

Pushes the contents of the local service directory to blob storage, updates the recording.json with a new GUID.

Links:

- https://docs.python.org/3/library/zlib.html
- https://docs.python.org/3/library/archiving.html
- https://pypi.org/project/azure-storage-blob/
- https://docs.python.org/3/library/typing.html
- https://docs.python.org/3/library/argparse.html

## Configuration

```json
{
    "configuration": { 
        "blob_prefix": "<prefix before the targeting guid>",
        "recordings_directory_patterns": [ "<glob pattern array>" ],
        "storage_account": "<blob storage>",
        "storage_account_container": "<blob storage container>"
    },
    "targeting": {
        "guid": "<identifier of a blob uploaded to storage>"
    }
}
```