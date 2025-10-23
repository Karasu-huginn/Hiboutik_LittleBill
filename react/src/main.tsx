import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { createBrowserRouter, Outlet, RouterProvider } from 'react-router'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { Navigation } from './Navigation.tsx'
import { CustomerSalesSearch } from './CustomerSalesSearch.tsx'

const router = createBrowserRouter([
  {
    path: "/",
    element: (
      <>
        <Navigation />
        <main>
          <Outlet />
        </main>
      </>
    ),
    children: [
      {
        path: "/",
        element: <App />,
      },
      {
        path: "/customers",
        element: <CustomerSalesSearch />
      },
    ]
  }
]);

const query_client = new QueryClient();

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <QueryClientProvider client={query_client}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  </StrictMode>,
)
