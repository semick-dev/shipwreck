# shipwreck
An experiment with azure-storage-blob and using blob storage as an asset repository.

## In Practice

<example image here>

## Installation

`pip install git+https://github.com/semick-dev/shipwreck.git`

## Usage

To access blob storage, you _must_ set environment variable `STORAGE_KEY`, which should be a key that is compatible with your targeted `recording.json`.

```
usage: ship [-h] [-d DIRECTORY] [{push,pull,clear}]

This CLI app is used to push and pull service directory recordings back and forth to blob storage. A "reset"
operation is merely clearing all discovered recordings directories. Same as before a "pull" operation.

positional arguments:
  {push,pull,clear}     Uploading, downloading, or resetting, which do you need?

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        The directory context in which to begin the search for a recording.json. Crawls
                        upwards until it finds either a .git folder or recording.json. Not providing this
                        argument will start the search from os.getcwd().
```

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

## Demo

```
<use python39 venv>
git clone semick-dev/azure-sdk-for-python@experiment/test-blob-recording-storage
cd <cloned>/sdk/tables/azure-data-tables
pip install tox tox-monorepo git+https://github.com/semick-dev/shipwreck.git
pip install -r dev-requirements
ship pull
git status
tox -e whl -c ../../../eng/tox/tox.ini
```
