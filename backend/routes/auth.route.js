import express from 'express'
import { chekAuth, signUp, logIn, logOut } from '../controllers/auth.controller.js'
import {protectRoute} from '../middlewares/authMiddleware.js'

const router = express.Router()

router.post('/signup', signUp)
router.post('/login', logIn)
router.post('/logout', logOut)  
router.get('/checkAuth', protectRoute,  chekAuth)

export default router