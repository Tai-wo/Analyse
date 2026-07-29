import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Upload from "./pages/Upload";
import Datasets from "./pages/Datasets";
import Workspace from "./pages/Workspace";
import Features from "./pages/Features";
import Excel from "./pages/Excel";
import Python from "./pages/Python";
import SQL from "./pages/SQL";
import Tableau from "./pages/Tableau";
import Results from "./pages/Results";
import History from "./pages/History";
import Settings from "./pages/Settings";
function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/upload"
          element={<Upload />}
        />

        <Route
          path="/datasets"
          element={<Datasets />}
        />

        <Route
          path="/workspace/:id"
          element={<Workspace />}
        />
        <Route
    path="/features"
    element={<Features />}
/>

<Route
    path="/excel"
    element={<Excel />}
/>

<Route
    path="/python"
    element={<Python />}
/>

<Route
    path="/sql"
    element={<SQL />}
/>

<Route
    path="/tableau"
    element={<Tableau />}
/>

<Route
    path="/results"
    element={<Results />}
/>

<Route
    path="/history"
    element={<History />}
/>

<Route
    path="/settings"
    element={<Settings />}
/>
        

      </Routes>

    </BrowserRouter>
  );
}

export default App;