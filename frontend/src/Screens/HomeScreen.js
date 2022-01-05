import React, { useState, useEffect } from 'react';
import { Grid, TextField, InputAdornment, IconButton } from '@mui/material';
import ProfCard from '../Components/ProfCard';
import SearchIcon from '@mui/icons-material/Search';
import Loader from '../Components/Loader';
import { getProfessorDetails, setProfessorSepcialisation } from '../Actions/profActions';
import { useDispatch, useSelector } from 'react-redux';
import Paginate from '../Components/Paginate';

const HomeScreen = ({ history, match }) => {
  const keyword = match.params.keyword;
  const pageNumber = match.params.pageNumber || 1;

  const [specialisation, setSpecialisation] = useState('');

  const dispatch = useDispatch();

  const professorDetails = useSelector((state) => state.professorDetails);
  let { loading, error, data, page, pages } = professorDetails;

  useEffect(() => {
    dispatch(getProfessorDetails(keyword, pageNumber));
  }, [specialisation, keyword, pageNumber]);

  return (
    <>
      <Grid pt={2} container align="center" justifyContent="center">
        <Grid item xs={11} md={12} p={1}>
          <TextField
            label="Search"
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
              if (e.key === 'Enter') {
                if (e.target.value !== '') history.push(`/search/${e.target.value}`);
                else history.push('/');
              }
            }}
          />
        </Grid>
        {loading ? (
          <Loader />
        ) : (
          data &&
          data.map((prof) => {
            return <ProfCard data={prof} history={history} />;
          })
        )}
      </Grid>
      <Grid contaimer alignItems="center" justifyContent="center">
        <Grid item sx={{ margin: 4, ml: '25vw' }}>
          <Paginate page={page} pages={pages} keyword={keyword} history={history}></Paginate>
        </Grid>
      </Grid>
    </>
  );
};

export default HomeScreen;
