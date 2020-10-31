import React from 'react';
import { render } from '@testing-library/react';
import App from './App';

const testGroups = [{
  key: 'petstore',
  title: 'PET Store',
  apiSpec: 'https://petstore.swagger.io/v2/swagger.json'
}]

test('renders groups', () => {
  const { getByText } = render(<App groups={testGroups} />);
  const sidebarLink = getByText(/PET Store/i);
  expect(sidebarLink).toBeInTheDocument();
});
