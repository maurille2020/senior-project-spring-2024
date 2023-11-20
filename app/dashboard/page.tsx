"use client";

// react components
import React, { useEffect } from "react";
import { useRouter } from "next/navigation";

// global states

//components
import { useAuth } from "@/context/AuthContext";
import BarChartBox from "@/components/dashboard/BarChartBox";
import BigChartBox from "@/components/dashboard/BigChartBox";
import ChartBox from "@/components/dashboard/ChartBox";
import PieChartBox from "@/components/dashboard/PieChartBox";
import TopBox from "@/components/dashboard/TopBox";

// assets
import {
  barChartBoxRevenue,
  barChartBoxVisit,
  chartBoxConversion,
  chartBoxProduct,
  chartBoxRevenue,
  chartBoxUser,
} from "@/data";

type Props = {};

const Dashboard = (props: Props) => {
  const { user } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!user) {
      router.push("/login");
    }
  }, [router, user]);

  return (
    <div className="h-full w-full flex flex-col xl:flex-row items-center justify-center gap-4 p-4">
      <div className="h-auto md:h-[88vh] w-auto sm:w-4/6 xl:w-[23%] flex flex-col md:flex-row items-center justify-center gap-4">
        <div className="h-[88vh] md:h-full w-full flex flex-col items-center justify-center gap-4 ">
          <div className="h-4/6 w-full">
            <TopBox />
          </div>
          <div className="h-2/6 w-full ">
            <BarChartBox {...barChartBoxVisit} />
          </div>
        </div>
        <div className="h-auto md:h-[88vh] w-full flex xl:hidden flex-col items-center justify-center gap-4">
          <div className="h-4/6 w-full ">
            <PieChartBox />
          </div>
          <div className="h-[31.5%] w-full ">
            <BarChartBox {...barChartBoxRevenue} />
          </div>
        </div>
      </div>
      <div className="h-auto md:h-[88vh] w-auto sm:w-[760px] flex flex-col items-center justify-center gap-4">
        <div className="h-1/2 w-full grid md:grid-cols-2 md:grid-rows-2 gap-4 ">
          <ChartBox {...chartBoxUser} />
          <ChartBox {...chartBoxProduct} />
          <ChartBox {...chartBoxConversion} />
          <ChartBox {...chartBoxRevenue} />
        </div>
        <div className="h-1/2 w-full ">
          <BigChartBox />
        </div>
      </div>
      <div className="h-[88vh] w-auto sm:w-4/6 xl:w-[23%] xl:flex hidden flex-col items-center justify-center gap-4">
        <div className="h-4/6 w-full ">
          <PieChartBox />
        </div>
        <div className="h-2/6 w-full ">
          <BarChartBox {...barChartBoxRevenue} />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;

// {/* <div className="h-auto w-auto flex flex-col md:flex-row items-center justify-center gap-8 ">
// <div className="h-[90vh] md:h-[57vh] 2xl:h-[88vh] w-10/12 2xl:w-[25rem] flex flex-col items-center justify-center gap-8 border border-orange-600">
//   {/* <TopBox />
//   <BarChartBox {...barChartBoxVisit} /> */}
// </div>
// <div className="h-[90vh] md:h-[57vh] 2xl:h-[88vh] w-10/12 2xl:w-[22rem] flex 2xl:hidden flex-col items-center justify-center gap-8 border border-orange-600">
//   {/* <PieChartBox />
//   <BarChartBox {...barChartBoxRevenue} /> */}
// </div>
// </div>
// <div className="h-full md:h-[57vh] 2xl:h-[88vh] w-auto flex flex-col items-center justify-center gap-8border border-orange-600">
// <div className="h-full md:h-3/6 w-[20.5rem] md:w-[86%]  grid md:grid-cols-2 md:grid-rows-2 gap-4border border-orange-600">
//   {/* <ChartBox {...chartBoxUser} />
//   <ChartBox {...chartBoxProduct} />
//   <ChartBox {...chartBoxConversion} />
//   <ChartBox {...chartBoxRevenue} /> */}
// </div>
// {/* <BigChartBox /> */}
// </div>
// <div className="h-[88vh] w-[22rem] hidden 2xl:flex flex-col items-center justify-center gap-8 border border-orange-600">
// {/* <PieChartBox />
// <BarChartBox {...barChartBoxRevenue} /> */}
// </div> */}
