liststudents=[
    {
        "id":1,
        "name":"Nguyen Van A",
         "diemtoan": 7,
        "diemvan": 8,
        "diemhoa": 9,
     },
        {
        "id":2,
        "name":"Nguyen Van B",
         "diemtoan": 9,
        "diemvan": 9,
        "diemhoa": 6,
        },
     {
        "id":3,
        "name":"Nguyen Van C",
        "diemtoan": 7,
        "diemvan": 9,
        "diemhoa": 7,
     },
      {
        "id":4,
        "name":"Nguyen Van D",
        "diemtoan": 10,
        "diemvan": 7,
        "diemhoa": 7,
     },
      {
        "id":5,
        "name":"Nguyen Van E",
        "diemtoan": 9,
        "diemvan": 9,
        "diemhoa": 4,
     },
]


for diemso in liststudents:
    print(diemso)

print("Học sinh có điểm trung bình >5")
for hocsinh in liststudents:
    # Tính điểm trung bình
    diemtoan = hocsinh["diemtoan"]
    diemvan = hocsinh["diemvan"]
    diemhoa = hocsinh["diemhoa"]
    diem_trung_binh = (diemtoan + diemvan + diemhoa) / 3
    
    # Kiểm tra điểm trung bình
    if diem_trung_binh > 5:
        # In thông tin sinh viên
        print(f"ID: {hocsinh['id']}")
        print(f"Tên: {hocsinh['name']}")


print("Học sinh có điểm hóa <5")
for hocsinh in liststudents:
   
    if (hocsinh["diemhoa"] < 5):
        print(f"ID: {hocsinh['id']}")
        print(f"Tên: {hocsinh['name']}")
