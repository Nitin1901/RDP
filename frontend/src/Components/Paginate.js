import React from 'react';
import { Pagination, PaginationItem, Stack } from '@mui/material';
import { Link } from 'react-router-dom';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';

const Paginate = ({ pages, keyword = '', page, history }) => {
  const changeHandler = (event, val) => {
    if (keyword) {
      history.push(`/search/${keyword}/page/${val}`);
    } else {
      history.push(`/page/${val}`);
    }
  };
  return (
    pages > 1 && (
      <Stack spacing={5}>
        <Pagination color="primary" count={pages} page={page} onChange={changeHandler}></Pagination>
      </Stack>
    )
  );
};

export default Paginate;
