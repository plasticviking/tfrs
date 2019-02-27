import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import CheckBox from '../../app/components/CheckBox';

class CreditTransferTerms extends Component {
  render () {
    let content = [(
      <h3 className="terms-header" key="header">Signing Authority Declaration</h3>
    )];

    content = content.concat(this.props.referenceData.signingAuthorityAssertions.map(assertion => (
      <div className="terms" key={assertion.id}>
        <div id="credit-transfer-term" className="check">
          <CheckBox
            addToFields={this.props.addToFields}
            fields={this.props.fields.terms}
            id={assertion.id}
            toggleCheck={this.props.toggleCheck}
          />
        </div>
        <div>{assertion.description}</div>
      </div>
    )));

    return content;
  }
}

CreditTransferTerms.propTypes = {
  addToFields: PropTypes.func.isRequired,
  fields: PropTypes.shape({
    terms: PropTypes.array
  }).isRequired,
  toggleCheck: PropTypes.func.isRequired,
  referenceData: PropTypes.shape({
    signingAuthorityAssertions: PropTypes.arrayOf(PropTypes.shape),
    isFetching: PropTypes.bool,
    isSuccessful: PropTypes.bool
  }).isRequired
};

const mapStateToProps = state => ({
  referenceData: {
    signingAuthorityAssertions: state.rootReducer.referenceData.data.signingAuthorityAssertions,
    isFetching: state.rootReducer.referenceData.isFetching,
    isSuccessful: state.rootReducer.referenceData.success
  }
});

const mapDispatchToProps = dispatch => ({
});

export default connect(mapStateToProps, mapDispatchToProps)(CreditTransferTerms);
