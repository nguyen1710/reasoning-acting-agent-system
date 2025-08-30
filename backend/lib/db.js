import mongoose from "mongoose";

export const connectDB = async () => {
    try{
        const conn = await mongoose.connect(process.env.MONGO_URI)
        console.log(`Connect to DB successfull: ${conn.connection.host}`)
    }catch(error){
        console.log('Mongo connection error:', error)
    }
}