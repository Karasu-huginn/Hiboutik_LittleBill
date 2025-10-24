import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { createBrowserRouter, Outlet, RouterProvider } from 'react-router'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { Navigation } from './Navigation.tsx'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import { CustomerSearch } from './CustomerSearch.tsx'
import { CustomerSales } from './CustomerSales.tsx'
import { Login } from './Login.tsx'
import { Signup } from './Signup.tsx'

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
        element: <>
          <CustomerSearch />
        </>
      },
      {
        path: "/customer-sales/:customer_id",
        element: <>
          <CustomerSales />
        </>
      },
      {
        path: "/login",
        element: <>
          <Login />
        </>
      },
      {
        path: "/signup",
        element: <>
          <Signup />
        </>
      },
    ]
  }
]);

const query_client = new QueryClient();

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <QueryClientProvider client={query_client}>
      <RouterProvider router={router} />
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  </StrictMode>,
)
