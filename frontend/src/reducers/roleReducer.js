import ActionTypes from '../constants/actionTypes/Roles';

const roleRequest = (state = {
  didInvalidate: false,
  role: {},
  isFetching: false
}, action) => {
  switch (action.type) {
    case ActionTypes.GET_ROLE:
      return {
        ...state,
        didInvalidate: false,
        role: {},
        isFetching: true
      };
    case ActionTypes.RECEIVE_ROLE:
      return {
        ...state,
        didInvalidate: false,
        role: action.data,
        isFetching: false
      };
    default:
      return state;
  }
};



export { roleRequest };
