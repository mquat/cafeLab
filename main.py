from fastapi import FastAPI

app = FastAPI()

#아래는 서버 실행을 확인하기 위함, merge 후 삭제할 예정
@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}