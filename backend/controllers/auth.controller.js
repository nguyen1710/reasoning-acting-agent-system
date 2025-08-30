import express from 'express'
import User from "../models/user.model.js"
import bcryptjs from 'bcryptjs'
import { generateToken } from '../lib/utils.js'
export const signUp =  async (req, res) => {
    const {fullName, password, email} = req.body
    try {

        if(password.length < 8) {
            return res.status(400).json({success: false , message: "Password must have at least 8 characters"})
        }

        const user =await User.findOne({email})

        if(user) return res.status(400).json({success: false, message: 'Email already exists'})

        const salt = await bcryptjs.genSalt(10)
        const hashedPassword = await bcryptjs.hash(password, salt)

        const newUser = new User({
            fullName: fullName,
            password: hashedPassword,
            email: email
        })

        if(newUser) {
            // //generate token 
            // generateToken(newUser._id, res)
            await newUser.save()

            return res.status(201).json({
                success: true,
                user: {
                    _id: newUser._id,
                    fullName: newUser.fullName,
                    password: newUser.password,
                    email: newUser.email
                }
            })
        }
        else {
            return res.status(400).json({success: false, message: 'Invalid User data'})
        }

    } catch (error) {
        console.log("Error in signup controller:", error)
        return res.status(500).json({message: 'Internal server error'})
    }
}

const s = () => {
    console.log("Đăngnhập thành công")
}

export const logIn = async (req, res) => {
    const {email, password} = req.body

    try {
        const user = await User.findOne({email})
        
        await new Promise((resolve) => setTimeout(resolve, 3000));
        if(!user){
            return res.status(400).json({success: false, message: "Invalid user"})
        }

        const isPasswordCorrect = await bcryptjs.compare(password, user.password)
        if(!isPasswordCorrect)
            res.status(400).json({suceess: false, message: 'Password is not correct'})
        generateToken(user._id, res)

        return res.status(200).json({
                success: true,
                user: {
                    _id: user._id,
                    fullName: user.fullName,
                    password: user.password,
                    email: user.email
                }
            })
    } catch (error) {
        console.log("Error in login controller:", error)
        return res.status(500).json({message: 'Internal server error'})
    }
}

export const logOut = (req, res) => {
    try {
        res.cookie('jwt', '', {maxAge: 0})
        return res.status(200).json({message: 'Logout successfully'})

    } catch (error) {
         console.log("Error in logout controller:", error)
        return res.status(500).json({message: 'Internal server error'})
    }
    
}

export const chekAuth = async (req ,res) => {
    try {
        const user = await User.findById(req.userId).select("-password"); // bỏ password
        res.json(user);
    } catch (error) {
        res.status(500).json({ message: "Internal server error" });
    }
}
 
