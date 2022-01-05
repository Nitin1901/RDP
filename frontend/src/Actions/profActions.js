import {
  PROFESSOR_DETAILS_REQUEST,
  PROFESSOR_DETAILS_SUCCESS,
  PROFESSOR_DETAILS_FAIL,
  SET_PROFESSOR_SPECIALISATION,
  PROFESSOR_DETAIL_REQUEST,
  PROFESSOR_DETAIL_SUCCESS,
  PROFESSOR_DETAIL_FAIL,
} from '../Constants/profConstants';
import axios from 'axios';

export const getProfessorDetails = (keyword, pageNumber) => async (dispatch) => {
  try {
    dispatch({ type: PROFESSOR_DETAILS_REQUEST });
    const { data } = await axios.get(`/api/professors?keyword=${keyword}&pageNumber=${pageNumber}`);

    dispatch({
      type: PROFESSOR_DETAILS_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: PROFESSOR_DETAILS_FAIL,
      //Checking for error.response and error.response.data.message to check the errors coming from backen
      payload:
        error.response && error.response.data.message ? error.response.data.message : error.message,
    });
  }
};

export const setProfessorSepcialisation = (specialisation) => async (dispatch) => {
  dispatch({
    type: SET_PROFESSOR_SPECIALISATION,
    payload: specialisation,
  });
};

export const getProfessorDetail = (id) => async (dispatch) => {
  try {
    dispatch({ type: PROFESSOR_DETAIL_REQUEST });
    const { data } = await axios.get(`/api/professors/${id}`);

    dispatch({
      type: PROFESSOR_DETAIL_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: PROFESSOR_DETAIL_FAIL,
      //Checking for error.response and error.response.data.message to check the errors coming from backen
      payload:
        error.response && error.response.data.message ? error.response.data.message : error.message,
    });
  }
};
