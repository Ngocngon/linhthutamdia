# Cập nhật www/ từ bản dựng mới

www/ là bản chép của thư mục `dist/` (index.html + img/...) trên máy Mac: `~/Documents/LinhThuTamDia/dist/`.

1. Dựng lại dist như thường lệ (build.js) trên máy Mac.
2. Trong kho này, xoá nội dung cũ của www/ rồi chép mới:
   ```
   rm -rf www && cp -R ~/Documents/LinhThuTamDia/dist www
   ```
3. Kiểm nhanh: mở `www/index.html` bằng trình duyệt, game vào được sảnh.
4. Commit và đẩy lên main:
   ```
   git add -A && git commit -m "Đồng bộ www từ dist" && git push origin main
   ```
5. Workflow "Dựng APK Android" tự chạy (có thể mở tay ở tab Actions). Khi xanh, APK mới nằm ở Releases, bản "ban-thu-moi-nhat".

Ghi chú: không cần sửa mã game. Khi chạy ngoài artifact, game tự dùng localStorage và phòng chơi giả (mock), nên không có `app-shim.js`.
