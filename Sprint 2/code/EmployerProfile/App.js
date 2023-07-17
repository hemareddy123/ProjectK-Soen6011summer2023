import React from 'react';
import { MDBRow, MDBCol, MDBInput, MDBBtn } from 'mdb-react-ui-kit';

import './Form.css'; // Import the custom CSS file for form styling

const App = () => {
    return (
        <div className="form-container">
            <form className="custom-form">
                <h2 className="form-heading">Update your Profile</h2>

                <MDBRow className="form-row">
                    <MDBCol md={6}>
                        <MDBInput id="firstNameInput" label="First name" />
                    </MDBCol>
                    <MDBCol md={6}>
                        <MDBInput id="lastNameInput" label="Last name" />
                    </MDBCol>
                </MDBRow>

                <MDBInput className="form-input" id="organizationInput" label="Organization" />
                <MDBInput className="form-input" type="email" id="emailInput" label="Email" />
                <MDBInput className="form-input" type="tel" id="phoneInput" label="Phone" />

                <MDBInput
                    className="form-input"
                    textarea
                    id="additionalInfoInput"
                    rows={4}
                    label="Additional information"
                />

                <MDBBtn className="form-button" type="submit" block>
                    Update
                </MDBBtn>
            </form>
        </div>
    );
};

export default App;
