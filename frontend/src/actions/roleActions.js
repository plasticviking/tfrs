import axios from 'axios';

import ActionTypes from '../constants/actionTypes/Roles';
import ReducerTypes from '../constants/reducerTypes/Roles';
import * as Routes from '../constants/routes';

const getRole = id => (dispatch) => {
  dispatch(getRoleRequest());

  axios.get(`${Routes.BASE_URL}${Routes.ROLES.API}/${id}`)
    .then((response) => {
      dispatch(getRoleSuccess(response.data));
    }).catch((error) => {
      dispatch(getRoleError(error.response));
    });
};

const getRoleError = error => ({
  errorMessage: error,
  name: ReducerTypes.ERROR_ROLE_REQUEST,
  type: ActionTypes.ERROR
});

const getRoleRequest = () => ({
  name: ReducerTypes.GET_ROLE_REQUEST,
  type: ActionTypes.GET_ROLE
});

const getRoleSuccess = organization => ({
  data: organization,
  name: ReducerTypes.RECEIVE_ROLE_REQUEST,
  receivedAt: Date.now(),
  type: ActionTypes.RECEIVE_ROLE
});

export { getRole };
