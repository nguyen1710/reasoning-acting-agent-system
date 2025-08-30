import jwt from "jsonwebtoken";

export const protectRoute = (req, res, next) => {
  try {
    const token = req.cookies.jwt; // lấy jwt từ cookie

    if (!token) {
      return res.status(401).json({ message: "Không có token, chưa đăng nhập" });
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.userId = decoded.userId; // lưu userId vào request
    next();
  } catch (error) {
    console.log("Error in protectRoute:", error);
    res.status(401).json({ message: "Token không hợp lệ" });
  }
};