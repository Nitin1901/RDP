import path from "path";
import express from "express";
import colors from "colors";
import dotenv from "dotenv";
import connectDB from "./config/db.js";
import profRouter from "./routes/profRoutes.js";
import { errorHandler, notFound } from "./middlewares/errorMiddleware.js";
import cors from "cors";
dotenv.config();

connectDB();

const app = express();

//Body Parser
app.use(express.json());

app.use(cors({ origin: true, credentials: true }));

app.use("/api/professors", profRouter);

//If the request doesn't match any uri here, then it goes to notFound and gets 404 not found message passed to errorHandler
app.use(notFound);
//Error handler handles errors and passes a json error message isntead of a html page
app.use(errorHandler);

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(
    `Server Running at port ${PORT} in ${process.env.NODE_ENV} mode`.yellow.bold
  );
});
