/*
 * Presentational component
 */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import FontAwesomeIcon from '@fortawesome/react-fontawesome';

import CreditTransactionRequestFormDetails from './CreditTransactionRequestFormDetails';
import Errors from '../../app/components/Errors';
import history from '../../app/History';
import * as Lang from '../../constants/langEnUs';
import DOCUMENT_STATUSES from '../../constants/documentStatuses';

class CreditTransactionRequestForm extends Component {
  componentDidMount () {
    this.props.getCompliancePeriods();
  }

  render () {
    return (
      <div className="credit-transaction-requests">
        <h1>{this.props.edit ? 'Edit' : 'New'} {this.props.documentType ? this.props.documentType.description : ''} Submission</h1>
        <form
          onSubmit={(event, status) =>
            this.props.handleSubmit(event, DOCUMENT_STATUSES.draft)}
        >
          <CreditTransactionRequestFormDetails
            categories={this.props.categories}
            compliancePeriods={this.props.referenceData.compliancePeriods}
            documentType={this.props.documentType}
            edit={this.props.edit}
            fields={this.props.fields}
            handleInputChange={this.props.handleInputChange}
          />

          {Object.keys(this.props.errors).length > 0 &&
            <Errors errors={this.props.errors} />
          }

          <div className="credit-transaction-requests-actions">
            <div className="btn-container">
              <button
                className="btn btn-default"
                onClick={() => history.goBack()}
                type="button"
              >
                <FontAwesomeIcon icon="arrow-circle-left" /> {Lang.BTN_APP_CANCEL}
              </button>
              {this.props.availableActions.includes('Cancelled') &&
                <button
                  className="btn btn-danger"
                  data-target="#confirmDelete"
                  data-toggle="modal"
                  type="button"
                >
                  <FontAwesomeIcon icon="minus-circle" /> {Lang.BTN_DELETE_DRAFT}
                </button>
              }
              {this.props.availableActions.includes('Draft') &&
              <button
                className="btn btn-default"
                type="submit"
              >
                <FontAwesomeIcon icon="save" /> {Lang.BTN_SAVE_DRAFT}
              </button>
              }
              {this.props.availableActions.includes('Submitted') &&
              <button
                className="btn btn-primary"
                data-target="#confirmSubmit"
                data-toggle="modal"
                type="button"
              >
                <FontAwesomeIcon icon="upload" /> Submit
              </button>
              }
            </div>
          </div>
        </form>
      </div>
    );
  }
}

CreditTransactionRequestForm.defaultProps = {
  edit: false,
  id: 0
};

CreditTransactionRequestForm.propTypes = {
  availableActions: PropTypes.arrayOf(PropTypes.string).isRequired,
  categories: PropTypes.arrayOf(PropTypes.shape()).isRequired,
  referenceData: PropTypes.shape({
    compliancePeriods: PropTypes.arrayOf(PropTypes.shape),
    isFetching: PropTypes.bool,
    isSuccessful: PropTypes.bool
  }).isRequired,
  edit: PropTypes.bool,
  errors: PropTypes.shape({}).isRequired,
  documentType: PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.shape({
      description: PropTypes.string,
      theType: PropTypes.string
    })
  ]).isRequired,
  fields: PropTypes.shape({
    comment: PropTypes.string
  }).isRequired,
  handleInputChange: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  id: PropTypes.number
};

const mapStateToProps = state => ({
  referenceData: {
    compliancePeriods: state.rootReducer.referenceData.data.compliancePeriods,
    isFetching: state.rootReducer.referenceData.isFetching,
    isSuccessful: state.rootReducer.referenceData.success
  }
});

const mapDispatchToProps = dispatch => ({
});

export default connect(mapStateToProps, mapDispatchToProps)(CreditTransactionRequestForm);
