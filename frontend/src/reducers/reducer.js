import { routerReducer as routing } from 'react-router-redux';
import { combineReducers } from 'redux';

import { approvedCreditTransfers, creditTransfer, creditTransfers } from './creditTransferReducer';
import { userRequest, userViewRequest, userAdmin } from './userReducer';

import { organizationRequest, organizations, organizationMembers, fuelSuppliersRequest } from './organizationReducer';
import errorRequest from './errorReducer';
import { documentUpload, documentUploads } from './documentUploadReducer';
import { roleRequest } from './roleReducer';
import { notifications, subscriptions } from './notificationReducer';
import { referenceData } from './referenceDataReducer';
import sessionTimeout from './sessionTimeoutReducer';

const rootReducer = combineReducers({
  approvedCreditTransfers,
  creditTransfer,
  creditTransfers,
  documentUpload,
  documentUploads,
  errorRequest,
  fuelSuppliersRequest,
  notifications,
  organizationMembers,
  organizationRequest,
  organizations,
  referenceData,
  roleRequest,
  routing,
  sessionTimeout,
  subscriptions,
  userAdmin,
  userRequest,
  userViewRequest
});

export default rootReducer;
