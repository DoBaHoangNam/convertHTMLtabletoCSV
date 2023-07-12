import csv
from bs4 import BeautifulSoup

# Đường dẫn tới tệp HTML đầu vào
input_file = 'path/to/input.html'

# Đường dẫn tới tệp CSV đầu ra
output_file = 'path/to/output.csv'

# Đọc nội dung tệp HTML
with open(input_file, 'r') as f:
    html_content = f.read()

# Phân tích cú pháp HTML với BeautifulSoup
soup = BeautifulSoup(html_content)

# Tìm tất cả các thẻ <tr> trong HTML
rows = soup.findAll('tr')

# Mở tệp CSV đầu ra
with open(output_file, 'w') as f:
    csv_writer = csv.writer(f)

    # Ghi dữ liệu vào tệp CSV
    for row in rows:
        # Lấy nội dung từ các ô trong hàng
        cells = row.findAll(['th', 'td'])
        row_data = [cell.text.strip() for cell in cells]
        csv_writer.writerow(row_data)

print("Chuyển đổi thành công.")
