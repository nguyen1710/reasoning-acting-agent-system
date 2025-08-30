import express from 'express'
import dotenv from 'dotenv'
import authRoutes from './routes/auth.route.js'
import {connectDB} from './lib/db.js'
import cookieParser from 'cookie-parser'
import cors from 'cors'
const app = express()
dotenv.config()
const PORT = process.env.PORT || 5000

app.use(cookieParser())
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.use(
  cors({
    origin: "http://localhost:5173", // chấp nhận frontend
    credentials: true, // 👈 cho phép gửi cookie
  })
);

app.use("/api/auth", authRoutes)

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`)
    connectDB()
})