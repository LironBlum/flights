## flights
# Run the app with: `uvicorn app.main:app --reload`

# server api requests samples
curl -X POST "http://127.0.0.1:8000/flight/add_flight/" \
-H "Content-Type: application/json" \
-d '{
  "Flight_id": "a21",
  "Arrival": "16:00",
  "Departure": "15:30"
}'

curl -X GET "http://127.0.0.1:8000/flight/get_flight/L123"

curl -X GET "http://127.0.0.1:8000/flight/get_flight/"
