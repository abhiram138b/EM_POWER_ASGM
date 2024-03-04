
# Asset Performance DashboardAPI



The Asset Performance Dashboard API facilitates CRUD (Create, Read, Update, Delete) operations to efficiently manage assets and their corresponding performance metrics. This API empowers users to interact seamlessly with asset data stored in a MongoDB database.
## Technologies Used

- **FastAPI**: FastAPI stands as a contemporary, high-performance web framework designed for swiftly constructing APIs using Python.
- **MongoDB**:MongoDB is a NoSQL database program that employs JSON-like documents, optionally utilizing schemas.

## Run Locally
### Running from source
To locally run the Asset Performance Dashboard API, ensure you have Python and MongoDB installed on your system. Follow these steps to set up and execute the API within a virtual environment.
1. Clone the Repository: 
    ``` 
   git clone https://github.com/your-username/asset-performance-dashboard.git
   cd asset-performance-dashboard
    ```

2. Create and activate virtual environment: 
   ```
    python3 -m venv myenv
    source myenv/bin/activate
   ```
    
3.Install the required packages:
    ```
    pip install -r requirements.txt  
    ```

4.Start the server:
```
python populate_db.py
uvicorn main:app --host "0.0.0.0" --port 8000
```
5.Run a HttpClient or visit [http://localhost:8000/docs] to interact with the api provided

## API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /create_asset/ | creates a new asset in the db |
| GET | /read_asset/{asset_id}| reads an  asset with given asset_id|
| PUT | /update_asset/ | updates an asset |
| DELETE| /delete_asset/{asset)id} | deletes an asset with given asset_id |
| POST | /create_pm/ | creates a new performanceMetric in the db |
| GET | /read_pm/{asset_id}| reasd a performanceMetric for a given asset_id|
| PUT | /update_pm/ | updates a performanceMetric |
| DELETE| /delete_pm/{asset_id} | deletes a performanceMetric with given asset_id |
| GET | /stats/ | Get the summary statistics for the Assets |




