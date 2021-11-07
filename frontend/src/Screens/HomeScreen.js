import React, { useState, useEffect } from "react";
import { Grid, TextField, InputAdornment, IconButton } from "@mui/material";
import ProfCard from "../Components/ProfCard";
import SearchIcon from "@mui/icons-material/Search";
import Loader from "../Components/Loader";
import {
  getProfessorDetails,
  setProfessorSepcialisation,
} from "../Actions/profActions";
import { useDispatch, useSelector } from "react-redux";

const HomeScreen = () => {
  const [specialisation, setSpecialisation] = useState("");

  const dispatch = useDispatch();

  const professorDetails = useSelector((state) => state.professorDetails);
  let { loading, error, professorInfo: data } = professorDetails;

  useEffect(() => {
    if (!data) {
      dispatch(getProfessorDetails());
    }
  }, [specialisation]);

  return (
    <>
      <Grid pt={2} container align="center" justifyContent="center">
        <Grid item xs={11} md={12} p={1}>
          <TextField
            label="Specialisation"
            type="text"
            fullWidth
            margin="dense"
            color="primary"
            InputProps={{
              startAdornment: (
                <InputAdornment>
                  <IconButton>
                    <SearchIcon />
                  </IconButton>
                </InputAdornment>
              ),
            }}
            onKeyPress={(e) => {
              if (e.key === "Enter") {
                setSpecialisation(e.target.value);
                dispatch(setProfessorSepcialisation(e.target.value));
              }
            }}
          />
        </Grid>
        {loading ? (
          <Loader />
        ) : specialisation === "" ? (
          data &&
          data.slice(0, 50).map((prof) => {
            return <ProfCard data={prof} />;
          })
        ) : (
          data &&
          data.map((prof) => {
            return <ProfCard data={prof} />;
          })
        )}
      </Grid>
    </>
  );
};

export default HomeScreen;
