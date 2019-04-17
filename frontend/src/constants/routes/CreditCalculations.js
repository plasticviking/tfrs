const BASE_PATH = '/admin/credit_calculation';
const API_BASE_PATH = '/credit_calculation';

const CREDIT_CALCULATIONS = {
  CARBON_INTENSITIES: `${BASE_PATH}/carbon_intensity_limits`,
  CARBON_INTENSITIES_API: `${API_BASE_PATH}/carbon_intensity_limits`,
  CARBON_INTENSITIES_DETAILS: `${BASE_PATH}/carbon_intensity_limits/view/:id`,
  CARBON_INTENSITIES_EDIT: `${BASE_PATH}/carbon_intensity_limits/edit/:id`,
  DEFAULT_CARBON_INTENSITIES: `${BASE_PATH}/default_carbon_intensities`,
  DEFAULT_CARBON_INTENSITIES_API: `${API_BASE_PATH}/default_carbon_intensities`,
  DEFAULT_CARBON_INTENSITIES_DETAILS: `${BASE_PATH}/default_carbon_intensities/view/:id`,
  DEFAULT_CARBON_INTENSITIES_EDIT: `${BASE_PATH}/default_carbon_intensities/edit/:id`,
  ENERGY_DENSITIES: `${BASE_PATH}/energy_densities`,
  ENERGY_DENSITIES_API: `${API_BASE_PATH}/energy_densities`,
  ENERGY_EFFECTIVENESS_RATIO: `${BASE_PATH}/energy_effectiveness_ratios`,
  ENERGY_EFFECTIVENESS_RATIO_API: `${API_BASE_PATH}/energy_effectiveness_ratios`,
  ENERGY_EFFECTIVENESS_RATIO_DETAILS: `${BASE_PATH}/energy_effectiveness_ratios/view/:id`,
  ENERGY_EFFECTIVENESS_RATIO_EDIT: `${BASE_PATH}/energy_effectiveness_ratios/edit/:id`,
  LIST: BASE_PATH
};

export default CREDIT_CALCULATIONS;
