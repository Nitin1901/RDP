import {
  PROFESSOR_DETAILS_REQUEST,
  PROFESSOR_DETAILS_SUCCESS,
  PROFESSOR_DETAILS_FAIL,
  SET_PROFESSOR_SPECIALISATION,
  PROFESSOR_DETAIL_REQUEST,
  PROFESSOR_DETAIL_SUCCESS,
  PROFESSOR_DETAIL_FAIL,
} from '../Constants/profConstants';

export const professorDetailsReducer = (state = {}, action) => {
  switch (action.type) {
    case PROFESSOR_DETAILS_REQUEST:
      return { loading: true, data: [] };
    case PROFESSOR_DETAILS_SUCCESS:
      return {
        loading: false,
        data: action.payload.data,
        page: action.payload.page,
        pages: action.payload.pages,
      };
    case PROFESSOR_DETAILS_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};

export const setProfessorSepcialisationReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_PROFESSOR_SPECIALISATION:
      return { specialisation: action.payload };

    default:
      return state;
  }
};

export const professorDetailReducer = (state = {}, action) => {
  switch (action.type) {
    case PROFESSOR_DETAIL_REQUEST:
      return { loading: true, professorInfo: null };
    case PROFESSOR_DETAIL_SUCCESS:
      return { loading: false, professorInfo: action.payload };
    case PROFESSOR_DETAIL_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};
